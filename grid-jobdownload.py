quit = False

def getAccessURL(subjob, numSubjobs=0):
    if quit:
        return

    if subjob.status != 'completed':
        print('Subjob {} not completed, skipping'.format(subjob.id))
        return

    try:
        print('Loading accessURL for {} of {}'.format(subjob.id, numSubjobs))
        return subjob.outputfiles[0].accessURL()[0]
    except:
        print('Error loading accessURL for {}.'.format(subjob.id))


def accessUrlsToFile(jobnumbers, nthread=6):
    """ save accessURLs of DIRAC joboutput files to textfiles named like the
    jobname.

    Args:
        jobnumbers (list[int], optional): jobs to store output from
        nthread (int): number of threads used to retreive the accessURL
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from os import path
    for jnumber in jobnumbers:
        print('Downloading job {}'.format(jnumber))
        name = jobs(jnumber).name
        numSubjobs = len(jobs(jnumber).subjobs)

        # create the threads
        pool = ThreadPoolExecutor(nthread)
        futures = [pool.submit(getAccessURL, sj, numSubjobs) for sj in jobs(jnumber).subjobs]

        # remove file before first iteration
        filename = name + '.txt'
        if path.isfile(filename):
            remove(filename)
        lineswritten = 0

        # append results to file as soon as ready
        for r in as_completed(futures):
            result = r.result()
            if result is not None:
                with open(filename, 'a') as f:
                    f.write(result + '\n') 
                    lineswritten += 1
            else:
                print('Subjob did not return output.')
        print('saved {} files for job {}'.format(lineswritten, jnumber))


def downloadSubjob(subjob, jobdir='', checksum=None, autoresubmit=True):
    from subprocess import check_output, CalledProcessError
    import os

    if quit:
        return False, subjob.id

    if subjob.status != 'completed':
        if subjob.status == 'failed' and autoresubmit:
            print('Resubmitting failed subjob {}.'.format(subjob.id))
            queues.add(subjob.resubmit)
            return False, subjob.id
        else:
            print('Subjob {} not completed, skipping.'.format(subjob.id))
            return False, subjob.id

    outputpath = os.path.join(jobdir, str(subjob.id) + '.root')
    if not os.path.isdir(os.path.dirname(outputpath)):
        os.makedirs(os.path.dirname(outputpath))

    if os.path.isfile(outputpath):
        print('file {} already exists, skipping'.format(outputpath))
        return False, subjob.id

    try:
        # build command
        cmd = ['xrdcp', '-N']
        if checksum is not None:
            cmd.append('-C')
            cmd.append(checksum)

        print('getting accessURL for subjob {}'.format(subjob.id))
        accessURL = subjob.outputfiles[0].accessURL()
        if len(accessURL) == 0:
            print('missing output URL, resubmitted subjob {}'.format(subjob.id))
            queues.add(subjob.resubmit)
            return False, subjob.id

        cmd.append(accessURL[0])
        cmd.append(outputpath)
        print('downloading outputfile for subjob {}'.format(subjob.id))
        output = check_output(cmd)
        return True, subjob.id
    except CalledProcessError as e:
        print('Could not copy subjob {} with error "{}".'.format(subjob.id, e))
        return False, subjob.id
    except Exception as e:
        print('An Exception occured while processing subjob {}: {}'.format(subjob.id, e))
        return False, subjob.id


def downloadGridToDir(jobnumbers, outputdir, nthread=6, checksum=None):
    """ download DIRAC joboutput of given jobs to outputdir

    Args:
        jobnumbers (list[int] or int): jobs to download
        outputdir (str): output directory. A subfolder (jobnumber.subjobnumber)
            will be created.
        nthread (int, optional): number of threads used to download
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import os

    if type(jobnumbers) == int:
        jobnumbers = [jobnumbers]

    for j in jobnumbers:
        name = jobs(j).name
        numSubjobs = len(jobs(j).subjobs)

        jdir = os.path.join(outputdir, str(j) + '-' + name)

        # prepare output directory
        if os.path.isdir(jdir):
            for _, _, files in os.walk(jdir):
                if files:
                    print('WARNING: Output directory is not empty!')
        else:
            os.makedirs(jdir)

        # create the threads
        pool = ThreadPoolExecutor(nthread)
        futures = [pool.submit(downloadSubjob, sj, jdir, checksum)
                for sj in jobs(j).subjobs]

        for r in as_completed(futures):
            status, sj = r.result()
            if status is True:
                print('job {}.{} downloaded successfully'.format(j, sj))
            else:
                print('job {}.{} could not be downloaded'.format(j, sj))

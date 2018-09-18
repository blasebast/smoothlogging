class smoothlogging(object):
    """
    This is class to make logging easier with writing to FS files

    Example usage is:
            from smoothLogging import smoothLogging

            lobj = smoothlogging()
            log = lobj.log("/path/to/log","testlog")
            log.info('log info')
            log.warning('log warning')
            log.error('log error')

    Above example will write log files to "/path/to/log/ directory with name alike: testlog_20170317125251.log
    """

    def log(self,logPath, rname):
        import logging
        import os
        import time
        logging.basicConfig(
                                    level=logging.DEBUG,
                                    format='%(asctime)-16s %(levelname)-8s %(message)s',
                                    datefmt='%Y-%m-%d %H:%M:%S',
                                    filename=os.path.join(logPath,'%s_%s.log') % (rname, time.strftime('%Y%m%d%H%M%S')),
                                    filemode='w')
        self.log_file_name = os.path.normpath(os.path.join(logPath,'%s_%s.log') % (rname, time.strftime('%Y%m%d%H%M%S')))
        self.logger = logging.StreamHandler()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)-16s %(levelname)-8s %(message)s')
        self.logger.setFormatter(self.formatter)
        logging.getLogger('').addHandler(self.logger)
        return logging

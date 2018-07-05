def init_logging(log_level=logging.INFO):
    log_format = '[%(levelname)s] %(asctime)s  %(filename)s line %(lineno)d: %(message)s'
    date_fmt = '%a, %d %b %Y %H:%M:%S'
    logging.basicConfig(
        format=log_format,
        datefmt=date_fmt,
        level=log_level,
    )
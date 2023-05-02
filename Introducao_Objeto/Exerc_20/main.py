class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        print(msg, 'FileMixin!!!!')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg, 'PrintMixin')


if __name__ == '__main__':
    lf = LogFileMixin()
    lf.log_error('ddd')
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
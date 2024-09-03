# Abstraçao
# se rodar essa classe, vai dar erro, pois nao pode usar. É pra usar apenas a subclasse que puxa essa
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')

# criando uma que possa ser usada e que herde da Log (que nao pode) 
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no log: {msg_formatada}')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que legal')

import os
import json
from flask import Flask,render_template,abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
class Files():
    directory = os.path.normpath(os.path.join(os.path.dirname(__file__),'..','files'))
    def __init__(self):
        self._file = self._read_file()
    def _read_file(self):
        result = {}
        for file_name in os.listdir(self.directory):
            file_path = os.path.join(self.directory,file_name)
            with open(file_path) as f:
                result[file_name[:-5]] = json.load(f)
        return result
    def get_title_list(self):
        return [item['title'] for item in  self._file.values()]
            
    def get_by_filename(self,filename):
        return self._file.get(filename)

files = Files()
@app.route('/')
def index():
    return render_template('index.html',title_list=files.get_title_list())
@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_by_filename(filename)
    if not file_item:
        abort(404)
    else:
        return render_template('file.html',file_item=files.get_by_filename(filename))
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
if __name__ == '__main__':
    app.run()

import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget, QPushButton, QTableWidget, QAbstractItemView, QHeaderView, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy
import qtawesome as qta
import wcwidth

enter = '\n'
blank = '    '
domain = '::'

class UtilsHelper():
    def format_text(text, width=30):
        count = wcwidth.wcswidth(text) - len(text)
        width = width - count if width >= count else 0
        fill = ' '
        return '{0:{1}{2}{3}}'.format(text, fill, '^', width)
    
class FileHelper():
    def gen_micro(class_name):
        micro = class_name + 'H'
        return micro
    
    def gen_head_h(class_name):
        micro = FileHelper.gen_micro(class_name)
        head = '#ifndef ' + micro + enter + '#define ' + micro + enter + enter
        return head
    
    def gen_tail_h(class_name):
        micro = FileHelper.gen_micro(class_name)
        tail = enter + '#endif' + ' // ' + micro
        return tail
    
    def gen_class_head(class_name):
        head = 'class ' + class_name + enter + '{' + enter
        return head
    
    def gen_class_tail():
        tail = '};' + enter
        return tail
    
    def gen_access_type(func_access_type, show_access_type):
        if (show_access_type != '1'):
            return ''
        type = func_access_type + ':' + enter
        return type

    def gen_func_param(func_param_name, semicolon=';'):
        print(type(func_param_name), func_param_name)
        real_param = '(' + func_param_name + ')' + semicolon

        return real_param
    
    def gen_func_h(func_return_type, func_name, func_param_name, semicolon=';'):
        real_param = FileHelper.gen_func_param(func_param_name, semicolon)
        func = blank + func_return_type + ' ' + func_name + real_param + enter
        return func
    
    def get_file_name_h(class_name):
        return class_name + ".h"
    
    def get_file_name_cpp(class_name):
        return class_name + ".cpp"
    
    def gen_head_cpp(class_name):
        head = '#include ' + '"' + FileHelper.get_file_name_h(class_name) + '"' + enter + enter
        return head
    
    def gen_func_cpp(class_name, func_return_type, func_name, func_param_name):
        real_param = FileHelper.gen_func_param(func_param_name, '')
        body = func_return_type + ' ' + class_name + \
            domain + func_name + real_param + enter
        body += '{' + enter
        body += '}' + enter
        return body
    
    def gen_file_h(class_name, func_define_list):
        with open(FileHelper.get_file_name_h(class_name), 'w') as f:
            #head
            head = FileHelper.gen_head_h(class_name)

            #body
            body = FileHelper.gen_class_head(class_name)

            for i in range(len(func_define_list)):
                func_param_name = func_define_list[i]["func_param_name"]
                func_access_type = func_define_list[i]["func_access_type"]
                show_access_type = func_define_list[i]["show_access_type"]

                func_return_type = func_define_list[i]["func_return_type"]
                func_name = func_define_list[i]["func_name"]

                access_type = FileHelper.gen_access_type(
                    func_access_type, show_access_type)
                func = FileHelper.gen_func_h(
                    func_return_type, func_name, func_param_name)
                body += access_type + func

            body += FileHelper.gen_class_tail()

            #tail
            tail = FileHelper.gen_tail_h(class_name)

            #content
            content = head + body + tail

            f.write(content)
            f.close()

    def gen_file_cpp(class_name, func_define_list):
        with open(FileHelper.get_file_name_cpp(class_name), 'w') as f:
            #head
            head = FileHelper.gen_head_cpp(class_name)

            #body
            body = ''
            size = len(func_define_list)
            for i in range(size):
                func_param_name = func_define_list[i]["func_param_name"]

                func_return_type = func_define_list[i]["func_return_type"]
                func_name = func_define_list[i]["func_name"]
                
                body += FileHelper.gen_func_cpp(class_name, func_return_type,
                                                func_name, func_param_name)

                if (i < size - 1):
                    body += enter

            #content
            content = head + body
            
            f.write(content)
            f.close()

    def gen_h_cpp(class_name, func_define_list):
        FileHelper.gen_file_h(class_name, func_define_list)
        FileHelper.gen_file_cpp(class_name, func_define_list)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.func_define_list = []

        self.widget_main = QWidget()
        self.layout_main = QGridLayout(self.widget_main)
        self.layout_main.setContentsMargins(0, 0, 0, 0)

        self.layout_class = QHBoxLayout()
        self.layout_func = QHBoxLayout()
        self.layout_result = QHBoxLayout()

        self.layout_main.addLayout(self.layout_class, 0, 0, 1, 2)
        self.layout_main.addLayout(self.layout_func, 1, 0, 1, 2)
        self.layout_main.addLayout(self.layout_result, 2, 0, 1, 2)

        self.setCentralWidget(self.widget_main)

        self.init_class()
        self.init_func()
        self.init_result()
        self.init_tab_order()

    def init_class(self):
        self.layout_class_left = QHBoxLayout()
        self.layout_class_right = QHBoxLayout()
        self.layout_class.addLayout(self.layout_class_left)
        self.layout_class.addLayout(self.layout_class_right)
        
        widget = QWidget(self)
        widget.setMinimumWidth(16)
        widget.setMaximumWidth(16)
        self.layout_class_left.addWidget(widget)

        label_class_name = QLabel()
        label_class_name.setText(UtilsHelper.format_text("类名:"))
        label_class_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_class_name.setMaximumWidth(64)
        self.layout_class_left.addWidget(label_class_name)

        self.edit_class_name = QLineEdit()
        self.edit_class_name.setMaximumWidth(128)
        self.edit_class_name.setMinimumHeight(32)
        self.edit_class_name.installEventFilter(self)
        self.layout_class_left.addWidget(self.edit_class_name)
        
        label_file_name = QLabel()
        label_file_name.setText(UtilsHelper.format_text("文件名:"))
        label_file_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_file_name.setMaximumWidth(64)
        self.layout_class_left.addWidget(label_file_name)

        self.edit_file_name = QLineEdit()
        self.edit_file_name.setMaximumWidth(128)
        self.edit_file_name.setMinimumHeight(32)
        self.edit_file_name.setReadOnly(True)
        self.layout_class_left.addWidget(self.edit_file_name)

        spacer = QSpacerItem(32, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_class_left.addItem(spacer)

        self.btn_add_func = QPushButton()
        self.btn_add_func.setText(UtilsHelper.format_text("增加函数"))
        self.btn_add_func.setMaximumWidth(96)
        self.btn_add_func.setMinimumHeight(32)
        self.btn_add_func.clicked.connect(self.on_add_func)
        self.layout_class_right.addWidget(self.btn_add_func)

        self.btn_sub_func = QPushButton()
        self.btn_sub_func.setText(UtilsHelper.format_text("减少函数"))
        self.btn_sub_func.setMaximumWidth(96)
        self.btn_sub_func.setMinimumHeight(32)
        self.btn_sub_func.clicked.connect(self.on_sub_func)
        self.layout_class_right.addWidget(self.btn_sub_func)

        self.btn_gen_cpp = QPushButton()
        self.btn_gen_cpp.setText(UtilsHelper.format_text("生成文件"))
        self.btn_gen_cpp.setMaximumWidth(96)
        self.btn_gen_cpp.setMinimumHeight(32)
        self.btn_gen_cpp.clicked.connect(self.on_gen_cpp)
        self.layout_class_right.addWidget(self.btn_gen_cpp)

        widget = QWidget(self)
        widget.setMinimumWidth(16)
        widget.setMaximumWidth(16)
        self.layout_class_right.addWidget(widget)

    def init_func(self):
        self.layout_func_left = QHBoxLayout()
        self.layout_func_right = QHBoxLayout()
        self.layout_func.addLayout(self.layout_func_left)
        self.layout_func.addLayout(self.layout_func_right)
        
        widget = QWidget(self)
        widget.setMinimumWidth(16)
        widget.setMaximumWidth(16)
        self.layout_func_left.addWidget(widget)

        label_return_name = QLabel()
        label_return_name.setText(UtilsHelper.format_text("返回值:"))
        label_return_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_return_name.setMaximumWidth(64)
        self.layout_func_left.addWidget(label_return_name)

        self.edit_return_name = QLineEdit()
        self.edit_return_name.setMaximumWidth(128)
        self.edit_return_name.setMinimumHeight(32)
        self.edit_return_name.setMinimumHeight(32)
        self.layout_func_left.addWidget(self.edit_return_name)

        label_func_name = QLabel()
        label_func_name.setText(UtilsHelper.format_text("函数名:"))
        label_func_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_func_name.setMaximumWidth(64)
        self.layout_func_left.addWidget(label_func_name)

        self.edit_func_name = QLineEdit()
        self.edit_func_name.setMaximumWidth(128)
        self.edit_func_name.setMinimumHeight(32)
        self.layout_func_left.addWidget(self.edit_func_name)

        label_param_name = QLabel()
        label_param_name.setText(UtilsHelper.format_text("入参:"))
        label_param_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_param_name.setMaximumWidth(64)
        self.layout_func_left.addWidget(label_param_name)

        self.edit_param_name = QLineEdit()
        self.edit_param_name.setMinimumHeight(32)
        self.edit_param_name.setMinimumHeight(32)
        self.layout_func_left.addWidget(self.edit_param_name)

        widget = QWidget(self)
        widget.setMinimumWidth(16)
        widget.setMaximumWidth(16)
        self.layout_func_right.addWidget(widget)

    def init_result(self):
        widget = QWidget(self)
        widget.setMinimumWidth(10)
        widget.setMaximumWidth(10)
        self.layout_result.addWidget(widget)

        self.init_result_table()

        widget = QWidget(self)
        widget.setMinimumWidth(16)
        widget.setMaximumWidth(16)
        self.layout_result.addWidget(widget)

    def init_result_table(self):
        table_col_names = ['返回值', '函数名', '(', '入参[0...n]', ')', ';']

        self.table_result = QTableWidget(self.widget_main)
        self.layout_result.addWidget(self.table_result)
        
        self.table_result.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_result.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_result.setColumnCount(len(table_col_names))
        self.table_result.setHorizontalHeaderLabels(table_col_names)
        self.table_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_result.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
        #self.table_result.setColumnWidth(3, 300)

    def add_result_table(self, func_list):
        row = self.table_result.rowCount()
        self.table_result.setRowCount(row + 1)

        column = 0
        for item in func_list:
            item = QtWidgets.QTableWidgetItem(item)
            item.setFlags(item.flags and (~Qt.ItemFlag.ItemIsEditable))
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.table_result.setItem(row, column, item)

            column += 1

    def init_tab_order(self):
        self.setTabOrder(self.edit_class_name, self.edit_return_name)
        self.setTabOrder(self.edit_return_name, self.edit_func_name)
        self.setTabOrder(self.edit_func_name, self.edit_param_name)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key.Key_Tab:
                if watched == self.edit_class_name:
                    class_name = self.edit_class_name.text()
                    self.edit_file_name.setText(class_name + ".cpp")

        return super().eventFilter(watched, event)

    def on_add_func(self):
        func_list = []

        func_return_type = self.edit_return_name.text().strip()
        func_name = self.edit_func_name.text().strip()
        func_param_name = self.edit_param_name.text().strip()
        
        func_list.append(func_return_type)
        func_list.append(func_name)
        func_list.append('(')
        func_list.append(func_param_name)
        func_list.append(')')
        func_list.append(';')

        self.add_result_table(func_list)

        func_param = {}
        func_param["func_access_type"] = "public"
        func_param["show_access_type"] = "1" if len(self.func_define_list) == 0 else ""
        func_param["func_name"] = func_name
        func_param["func_return_type"] = func_return_type
        func_param["func_param_name"] = func_param_name
        func_param["func_param_type"] = ""
        self.func_define_list.append(func_param)

        self.reset_param()
        
        print('on_add_func: ', func_list)

    def on_sub_func(self):
        row = self.table_result.rowCount()
        self.table_result.setRowCount(row - 1)
        self.func_define_list.pop()
        print('on_sub_func')

    def on_gen_cpp(self):
        print(self.func_define_list)
        class_name = self.edit_class_name.text()
        FileHelper.gen_h_cpp(class_name, self.func_define_list)
        print('on_gen_cpp')

    def reset_param(self):
        self.edit_return_name.clear()
        self.edit_func_name.clear()
        self.edit_param_name.clear()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.setWindowIcon(qta.icon("mdi6.language-cpp"))
    window.setWindowTitle("C++类自动生成工具")
    window.resize(822, 450)
    window.show()

    sys.exit(app.exec())

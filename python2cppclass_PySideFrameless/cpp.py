enter = '\n'
blank = '    '
domain = '::'
    
class CppFileHelper():
    def gen_micro(class_name):
        micro = class_name + 'H'
        return micro

    def gen_head_h(class_name):
        micro = CppFileHelper.gen_micro(class_name)
        head = '#ifndef ' + micro + enter + '#define ' + micro + enter + enter
        return head

    def gen_tail_h(class_name):
        micro = CppFileHelper.gen_micro(class_name)
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
        real_param = CppFileHelper.gen_func_param(func_param_name, semicolon)
        func = blank + func_return_type + ' ' + func_name + real_param + enter
        return func

    def get_file_name_h(class_name):
        return class_name + ".h"

    def get_file_name_cpp(class_name):
        return class_name + ".cpp"

    def gen_head_cpp(class_name):
        head = '#include ' + '"' + \
            CppFileHelper.get_file_name_h(class_name) + '"' + enter + enter
        return head

    def gen_func_cpp(class_name, func_return_type, func_name, func_param_name):
        real_param = CppFileHelper.gen_func_param(func_param_name, '')
        body = func_return_type + ' ' + class_name + \
            domain + func_name + real_param + enter
        body += '{' + enter
        body += '}' + enter
        return body

    def gen_file_h(class_name, func_define_list):
        with open(CppFileHelper.get_file_name_h(class_name), 'w') as f:
            #head
            head = CppFileHelper.gen_head_h(class_name)

            #body
            body = CppFileHelper.gen_class_head(class_name)

            for i in range(len(func_define_list)):
                func_param_name = func_define_list[i]["func_param_name"]
                func_access_type = func_define_list[i]["func_access_type"]
                show_access_type = func_define_list[i]["show_access_type"]

                func_return_type = func_define_list[i]["func_return_type"]
                func_name = func_define_list[i]["func_name"]

                access_type = CppFileHelper.gen_access_type(
                    func_access_type, show_access_type)
                func = CppFileHelper.gen_func_h(
                    func_return_type, func_name, func_param_name)
                body += access_type + func

            body += CppFileHelper.gen_class_tail()

            #tail
            tail = CppFileHelper.gen_tail_h(class_name)

            #content
            content = head + body + tail

            f.write(content)
            f.close()

    def gen_file_cpp(class_name, func_define_list):
        with open(CppFileHelper.get_file_name_cpp(class_name), 'w') as f:
            #head
            head = CppFileHelper.gen_head_cpp(class_name)

            #body
            body = ''
            size = len(func_define_list)
            for i in range(size):
                func_param_name = func_define_list[i]["func_param_name"]

                func_return_type = func_define_list[i]["func_return_type"]
                func_name = func_define_list[i]["func_name"]

                body += CppFileHelper.gen_func_cpp(class_name, func_return_type,
                                                func_name, func_param_name)

                if (i < size - 1):
                    body += enter

            #content
            content = head + body

            f.write(content)
            f.close()

    def gen_h_cpp(class_name, func_define_list):
        CppFileHelper.gen_file_h(class_name, func_define_list)
        CppFileHelper.gen_file_cpp(class_name, func_define_list)
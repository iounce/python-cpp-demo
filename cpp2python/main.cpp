#include "Python.h"
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <windows.h>

using namespace std;

std::string utf82gbk(const std::string &strUtf8)
{
    string outGBK = "";
    
    int n = MultiByteToWideChar(CP_UTF8, 0, strUtf8.c_str(), -1, NULL, 0);
    WCHAR *str1 = new WCHAR[n];
    
    MultiByteToWideChar(CP_UTF8, 0, strUtf8.c_str(), -1, str1, n);
    n = WideCharToMultiByte(CP_ACP, 0, str1, -1, NULL, 0, NULL, NULL);
    
    char *str2 = new char[n];
    WideCharToMultiByte(CP_ACP, 0, str1, -1, str2, n, NULL, NULL);
   
    outGBK = str2;

    delete[] str1;
    str1 = NULL;

    delete[] str2;
    str2 = NULL;

    return outGBK;
}

int main()
{
    Py_Initialize();
    
    int ret = Py_IsInitialized();
    if (ret == 0)
    {
        cout << "Initialize error: " << ret << endl;
        return 0;
    }

    PyObject *module = PyImport_ImportModule("main");
    if (module == nullptr)
    {
        return 0;
    }

    PyObject *sayHello = PyObject_GetAttrString(module, "sayHello");
    if (sayHello == nullptr || !PyCallable_Check(sayHello))
    {
        cout << "Can't find funftion (sayHello)" << endl;
        return 0;
    }

    PyObject *result = PyObject_CallObject(sayHello, nullptr);
    if (result == nullptr)
    {
        cout << "Call function failed" << endl;
        return 0;
    }

    if (PyUnicode_Check(result))
    {
        const char *data = PyUnicode_AsUTF8(result);
        cout << utf82gbk(data) << endl;
    }

    PyObject *addValue = PyObject_GetAttrString(module, "addValue");
    if (addValue == nullptr || !PyCallable_Check(addValue))
    {
        cout << "Can't find funftion (addValue)" << endl;
        return 0;
    }

    PyObject *args = PyTuple_New(2);

    PyObject *value1 = Py_BuildValue("i", 111);
    PyObject *value2 = Py_BuildValue("i", 222);

    PyTuple_SetItem(args, 0, value1);
    PyTuple_SetItem(args, 1, value2);

    result = PyObject_CallObject(addValue, args);
    if (result == nullptr)
    {
        cout << "Call function failed" << endl;
        return 0;
    }

    if (PyLong_Check(result))
    {
        int data = PyLong_AsLong(result);
        cout << data << endl;
    }

    Py_Finalize();

    return 0;
}
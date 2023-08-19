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

class AutoReference
{
public:
    AutoReference()
    {
    }
    AutoReference(PyObject *obj, bool addRef = false)
    {
        addObj(obj, addRef);
    }
    ~AutoReference()
    {
        for (size_t i = 0; i < m_objs.size(); i++)
        {
            PyObject *obj = m_objs[i];
            if (obj != nullptr)
            {
                Py_DECREF(obj);
                obj = nullptr;
            }
        }

        m_objs.clear();
    }

    void addObj(PyObject *obj, bool addRef = false)
    {
        if (addRef)
        {
            Py_INCREF(obj);
        }

        m_objs.push_back(obj);
    }
private:
    vector<PyObject *> m_objs;
};

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

    AutoReference autoRef(module);

    {
        PyObject *sayHello = PyObject_GetAttrString(module, "sayHello");
        if (sayHello == nullptr || !PyCallable_Check(sayHello))
        {
            cout << "Can't find funftion (sayHello)" << endl;
            return 0;
        }

        AutoReference autoRef;

        autoRef.addObj(sayHello);

        PyObject *result = PyObject_CallObject(sayHello, nullptr);
        if (result == nullptr)
        {
            cout << "Call function failed" << endl;
            return 0;
        }

        autoRef.addObj(result);

        if (PyUnicode_Check(result))
        {
            const char *data = PyUnicode_AsUTF8(result);
            cout << utf82gbk(data) << endl;
        }
    }

    {
        PyObject *addValue = PyObject_GetAttrString(module, "addValue");
        if (addValue == nullptr || !PyCallable_Check(addValue))
        {
            cout << "Can't find funftion (addValue)" << endl;
            return 0;
        }

        AutoReference autoRef;

        autoRef.addObj(addValue);

        PyObject *args = PyTuple_New(2);

        PyObject *value1 = Py_BuildValue("i", 111);
        PyObject *value2 = Py_BuildValue("i", 222);

        PyTuple_SetItem(args, 0, value1);
        PyTuple_SetItem(args, 1, value2);

        autoRef.addObj(args);
        autoRef.addObj(value1);
        autoRef.addObj(value2);

        PyObject *result = PyObject_CallObject(addValue, args);
        if (result == nullptr)
        {
            cout << "Call function failed" << endl;
            return 0;
        }

        autoRef.addObj(result);

        if (PyLong_Check(result))
        {
            int data = PyLong_AsLong(result);
            cout << data << endl;
        }
    }

    {
        PyObject *int2str = PyObject_GetAttrString(module, "int2str");
        if (int2str == nullptr || !PyCallable_Check(int2str))
        {
            cout << "Can't find funftion (int2str)" << endl;
            return 0;
        }

        AutoReference autoRef;

        autoRef.addObj(int2str);

        PyObject *funcArgs = PyTuple_New(1);
        PyObject *listArgs = PyList_New(0);

        PyObject *intValue1 = Py_BuildValue("i", 1);
        PyObject *intValue2 = Py_BuildValue("i", 2);
        PyObject *intValue3 = Py_BuildValue("i", 3);

        PyList_Append(listArgs, intValue1);
        PyList_Append(listArgs, intValue2);
        PyList_Append(listArgs, intValue3);

        autoRef.addObj(funcArgs);
        autoRef.addObj(listArgs);
        autoRef.addObj(intValue1);
        autoRef.addObj(intValue2);
        autoRef.addObj(intValue3);

        PyTuple_SetItem(funcArgs, 0, listArgs);

        PyObject *result = PyObject_CallObject(int2str, funcArgs);
        if (result == nullptr)
        {
            cout << "Call function failed" << endl;
            return 0;
        }

        autoRef.addObj(result);

        if (PyList_Check(result))
        {
            int size = PyList_Size(result);
            cout << "list size: " << size << endl;

            for (int i = 0; i < size; i++)
            {
                PyObject *item = PyList_GetItem(result, i);
                if (PyUnicode_Check(item))
                {
                    const char *data = PyUnicode_AsUTF8(item);
                    cout << data << endl;
                }
            }
        }
    }

    {
        PyObject *packOrder = PyObject_GetAttrString(module, "packOrder");
        if (packOrder == nullptr || !PyCallable_Check(packOrder))
        {
            cout << "Can't find funftion (packOrder)" << endl;
            return 0;
        }

        AutoReference autoRef;

        autoRef.addObj(packOrder);

        PyObject *orderArgs = PyTuple_New(1);
        PyObject *dictArgs = PyDict_New();

        PyObject *dvalue1 = Py_BuildValue("s", "10.12");
        PyObject *dvalue2 = Py_BuildValue("s", "200");

        PyDict_SetItemString(dictArgs, "input_price", dvalue1);
        PyDict_SetItemString(dictArgs, "input_volume", dvalue2);

        PyTuple_SetItem(orderArgs, 0, dictArgs);

        autoRef.addObj(orderArgs);
        autoRef.addObj(dictArgs);
        autoRef.addObj(dvalue1);
        autoRef.addObj(dvalue2);

        PyObject *result = PyObject_CallObject(packOrder, orderArgs);
        if (result == nullptr)
        {
            cout << "Call function failed" << endl;
            return 0;
        }

        autoRef.addObj(result);

        if (PyDict_Check(result))
        {
            PyObject * price = PyDict_GetItemString(result, "price");
            if (PyUnicode_Check(price))
            {
                const char *data = PyUnicode_AsUTF8(price);
                cout << data << endl;
            }

            PyObject * volume = PyDict_GetItemString(result, "volume");
            if (PyUnicode_Check(volume))
            {
                const char *data = PyUnicode_AsUTF8(volume);
                cout << data << endl;
            }

            PyObject * remark = PyDict_GetItemString(result, "remark");
            if (PyUnicode_Check(remark))
            {
                const char *data = PyUnicode_AsUTF8(remark);
                cout << data << endl;
            }
        }

        if (PyDict_Check(result))
        {
            Py_ssize_t pos = 0;
            PyObject *key = nullptr;
            PyObject *value = nullptr;

            cout << "............................" << endl;
            cout << "Dict: " << endl;
            while (PyDict_Next(result, &pos, &key, &value))
            {
                if (PyUnicode_Check(key))
                {
                    const char *data = PyUnicode_AsUTF8(key);
                    cout << data << ":";
                }

                if (PyUnicode_Check(value))
                {
                    const char *data = PyUnicode_AsUTF8(value);
                    cout << data << endl;
                }
            }
        }
    }

    Py_Finalize();

    getchar();

    return 0;
}
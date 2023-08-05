#ifndef __CLASS_H
#define __CLASS_H

#include <string>

class Base
{
public:
    Base()
    {
    }
    virtual ~Base()
    {
    }
protected:
    virtual bool valid() = 0;
public:
    int parse(int argc, char *argv[])
    {
        return 0;
    }

    void set(int value)
    {
        m_iValue = value;
    }

    void set(const std::string &value)
    {
        m_strValue = value;
    }
public:
    int m_iValue;
    std::string m_strValue;
    static int m_type;
};

int Base::m_type = 2023;

#endif
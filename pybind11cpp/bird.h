#ifndef __BIRD_H
#define __BIRD_H

#include <string>
#include <iostream>
using namespace std;

class Animal
{
public:
    Animal(): m_name("")
    {
    }

    Animal(const string& name) : m_name(name)
    {
    }

    ~Animal()
    {
    }

    const string& GetName()
    {
        return m_name;
    }
private:
    string m_name;
};

class Bird: public Animal
{
public:
    Bird(): Animal()
    {
    }

    Bird(const string& name): Animal(name)
    {
    }
public:
    void Fly()
    {
        cout << "Fly" << endl;
    }
};

#endif
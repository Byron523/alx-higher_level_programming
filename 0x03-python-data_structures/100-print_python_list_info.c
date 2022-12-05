#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints the python list info
* @p: Python object
* Return: nothing
*/
void print_python_list_info(Pyobject *p)
{
        long int size, i;
        PyListObject *list;
        PyObject *item;
        
        size = Py_SIZE(p);
        printf("[*] size of the Pyhton List = %ld\n", size);

        list = (PyListObject *)p;
        printf("[*] Allocated = %ld\n", list->allocated);
        
        for (i = 0; i < size; i++)
        {
                item = PyList_GetItem(p, i);
                printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
}

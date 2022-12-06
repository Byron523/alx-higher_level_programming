#include <stdio.h>
#include <listobject.h>
#include <Python.h>

/**
* print_python_list_info - prints the python list info
* @p: Python object
* Return: nothing
*/
void print_python_list_info(Pyobject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name);
}

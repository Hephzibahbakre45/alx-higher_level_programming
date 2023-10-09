#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print some basic
  info about python list
 * @p: python object
 **/

void print_python_list_info(PyObject *p)
{
	long int size;
	int i;
	PyListObject *obj;

	size = Py_SIZE(p);
	allocation = (PyListObject *)p->allocated

	printf("[*] Size of the python list = %li\n", size);
	printf("[*] Allocated = %li\n", allocation);

	for (i = 0; i < size; i++)
	{
	printf(" Element %d: ", i);

	obj = PyList_GetItem(p, i);
	printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

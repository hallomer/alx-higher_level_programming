#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: pointer to python opject
 *
 * Return: nothing
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *object;

	printf("[*] Size of the python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", (((PyListObject *)p)->allocated));

	for (i = 0; i < size; i++)
	{
		object = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(object)->tp_name);
	}
}

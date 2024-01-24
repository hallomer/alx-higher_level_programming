nclude <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	/* Get the size of the Python list */
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/* Iterate over each item in the list */
	for (i = 0; i < size; i++)
	{
		/* Get the item at index i */
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		/* Print the type name of the item */
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	/* Check if the object is a valid bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Get the size of the bytes object */
	size = PyBytes_Size(p);
	/* Get the string representation of the bytes object */
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	/* Print the first 10 bytes of the bytes object */
	for (i = 0; i < size && i < 10; i++)
		printf("%02x ", (unsigned char)str[i]);

	printf("\n");
}

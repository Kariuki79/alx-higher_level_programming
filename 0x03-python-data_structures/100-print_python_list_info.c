#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: Pointer to a Python object (PyObject)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t allocated;
	Py_ssize_t i;
	PyListObject *list;
	PyObject *item;

	/* Get the current size of the list using the CPython macro */
	size = Py_SIZE(p);

	/* Cast PyObject pointer to PyListObject to access list-specific fields */
	list = (PyListObject *)p;
	allocated = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	/* Loop through each element in the list */
	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

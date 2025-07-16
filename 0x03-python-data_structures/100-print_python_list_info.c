#include <Python.h>

/**
 * print_python_list_info - function print some info about python lists
 *
 * @p: python list object
 * Return: returns nothing
 */
void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type_name = Py_TYPE(item)->tp_name;

		printf("Element %zd: %s\n", i, type_name);
	}
}


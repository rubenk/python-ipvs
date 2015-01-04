#include "Python.h"
#include "libipvs.h"


static PyObject *ipvs_nr_services(PyObject *self, PyObject *args)
{
    return Py_BuildValue("l", ipvs_info.num_services);
}

static PyObject *ipvs_hashtable_size(PyObject *self, PyObject *args)
{
    return Py_BuildValue("l", ipvs_info.size);
}

static PyMethodDef module_methods[] = {
    {"nr_services", ipvs_nr_services, METH_NOARGS, "get number of services"},
    {"hashtable_size", ipvs_hashtable_size, METH_NOARGS, "get size of connection hashtable"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC initipvs(void)
{
    PyObject *module;

    module = Py_InitModule3("ipvs", module_methods, "python IPVS module");

    if (!module)
	return;
    if (ipvs_init() == -1)
        return;
}

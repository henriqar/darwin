#include<Python.h>

static char module_docstring[] = "module docstring";

// define all methods for the module _opt with its corresponding docstring
static PyObject * opt_test(PyObject *self, PyObject *args);
static char test_docstring[] = "Test method for the _opt module";

static PyMethodDef module_methods[] = {
  {"test", opt_test, METH_VARARGS, test_docstring},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _optmodule = { 
  PyModuleDef_HEAD_INIT,
  "_opt", // name of module
  module_docstring, // moduel docstring
  -1, // size of per interpreter state of module
  module_methods,
};

PyMODINIT_FUNC PyInit__opt(void) {
  PyObject * module = PyModule_Create(&_optmodule);
  return module == NULL ? NULL : module;
}

static PyObject * opt_test(PyObject *self, PyObject *args) {
  return NULL;
}

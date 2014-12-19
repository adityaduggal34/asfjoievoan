'''The control application allows you to have control variables/parameters
for the other applications in your project.

eg. If you are an institute and are not accepting a form. you may turn it off.
In the application containing the form you specify a control.py file which
contains 

import control
control_variable=control.models.variable()
control_variable.appname='admissionforms'
control_variable.name='accepting'
control_variable.value='False'
control_variable.save()


'''

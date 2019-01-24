import tango
import time

# time in seconds
t = 1

encoder_mirror = tango.DeviceProxy('b108a/ctl/ik220-02')
encoder_grating = tango.DeviceProxy('b108a/ctl/ik220-01')

sample = 4

value_buffer_mirror = []
value_buffer_grating = [] 

while(1):

    value_buffer_mirror.append(encoder_mirror.getAttribute('').value)
    value_buffer_grating.append(encoder_mirror.getAttribute('').value)

    if value_buffer_mirror[-1] == value_buffer_mirror[-2]:
        print('Same value for mirror encoder!  The value is:    {}'.format(value_buffer_mirror[-1]))
    if value_buffer_grating[-1] == value_buffer_grating[-2]:
        print('Same value for grating encoder! The value is:    {}'.format(value_buffer_grating[-1]))
    if len(value_buffer_mirror) > sample:
        value_buffer_mirror = value_buffer_mirror[1:]
    if len(value_buffer_grating) > sample:
        value_budder_grating = value_buffer_grating[1:]

    time.sleep(t)

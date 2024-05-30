import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    abb.send_and_wait(rrc.SetTool('t_A061_InlineMixer'))
    done = abb.send_and_wait(rrc.PrintText('tool set'))
    print('Tool set = ', done)

    abb.send_and_wait(rrc.SetWorkObject('ob_A061_Wobjdata'))
    done = abb.send_and_wait(rrc.PrintText('workobject set'))
    print('Workobject set = ', done)

    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())
    print(frame, external_axes)

    frame.xaxis = [-1, 0, 0]
    frame.yaxis = [0, 1, 0]
    
    done = abb.send_and_wait(rrc.MoveToRobtarget(frame, external_axes, 100, rrc.Zone.FINE))

    # End of Code
    print('Finished')

    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())
    print(frame, external_axes)

    # Close client
    ros.close()
    ros.terminate()
    print('Disconnected')

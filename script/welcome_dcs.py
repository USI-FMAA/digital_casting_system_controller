import compas_rrc as rrc

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    done = abb.send_and_wait(rrc.PrintText('Welcome to COMPAS_RRC'))

    # Print feedback
    print('Feedback = ', done)

    abb.send_and_wait(rrc.SetTool('t_A061_InlineMixer'))
    done = abb.send_and_wait(rrc.PrintText('tool set'))
    print('Tool set = ', done)

    abb.send_and_wait(rrc.SetWorkObject('ob_A061_Wobjdata'))
    done = abb.send_and_wait(rrc.PrintText('workobject set'))
    print('Workobject set = ', done)

    frame, external_axes = abb.send_and_wait(rrc.GetRobtarget())
    print(frame, external_axes)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()
    
    print('disconnected')

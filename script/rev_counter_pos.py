import compas_rrc as rrc

if __name__ == '__main__':

    """
    This script is to move robot to a rev counter position and get the joints values.
    """
    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Print text on FlexPenant
    done = abb.send_and_wait(rrc.PrintText('Welcome to COMPAS_RRC'))

    # Move to position
    move = abb.send_and_wait(rrc.MoveToJoints([0,0,0,0,0,0], [], 1000, rrc.Zone.FINE))

    # Get joints
    robot_joints, external_axes = abb.send_and_wait(rrc.GetJoints())

    # Print received values
    print(robot_joints, external_axes)

    # Print feedback
    print('Feedback = ', done)

    # End of Code
    print('Finished')

    # Close client
    ros.close()
    ros.terminate()

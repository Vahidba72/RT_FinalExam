#! /usr/bin/env python3

# Import necessary libraries
import rospy

from assignment_2_2023.srv import CancelService, CancelServiceResponse, CancelServiceRequest



import actionlib
import actionlib.msg
import assignment_2_2023.msg



from actionlib_msgs.msg import GoalStatus

def cancel_target(req):

	global client

	

	res = CancelServiceResponse()
	
	
	
	client.cancel_goal()
	
	
	
	
	
	
	
	res.x_target= rospy.get_param('/des_pos_x',default=0.0)
	res.y_target = rospy.get_param('/des_pos_y',default=0.0)
	
	rospy.loginfo("Cancel goal: target_x = %f, target_y = %f", x_t , y_t")
	
	
	
	return res

def main():

	global client


	# Initialize the node 
	rospy.init_node("node_d_service")
	rospy.loginfo("Cancel started and ready to cancel the movement on command")
	
	client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2023.msg.PlanningAction)	
	client.wait_for_server()
	
	rospy.Service('cancellation', CancelService, cancel_target) 
	
	
		
	rospy.spin()
	
	
if __name__ == "__main__":

	a = main()

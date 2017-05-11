#!/bin/bash
#./send_packet.py &
hashpipe -p demo2_hashpipe -I 2 -c 0 demo2_net_thread -c 1 demo2_gpu_thread -c 2 demo2_output_thread 

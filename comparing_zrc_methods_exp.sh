#! /bin/bash 
# TODO enable debugging mode, and save logs /error logs in different files.
echo -e "\n ######## COMPARING ZRC METHODS ######## \n"
echo -n "> executing the note_detection script.."
python -m experiments.note_detection 2>&1 1>/dev/null 
echo "finished."
echo -n "> plotting the results.."
gnuplot experiments/zcr_comp_plot.dem 2>&1 1>/dev/null
echo  "finished."
echo -n "> opening the graph.." 
open experiments/comparing_zcr_methods.png 2>&1 1>/dev/null
echo "finished."
echo -n "> opening one of the sig graphs.." 
open experiments/waves/a2.png 2>&1 1>/dev/null
echo "finished."

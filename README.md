# outputFilesGenerator
<strong>Competitive Programmers</strong> often need to generate a lot of test cases for the problems they have curated. Generating input files is a task which is very difficult to automate, because of the fact that the constraints for all the input files are not the same. But the task of generating the output files based on the inputs from the input files can be simplified. 

Let us consider that you have a directory containing the <b>soln.cpp</b>(the file from which the outputs need to be generated) file and the input.txt files, say of the form <strong>input0.txt</strong>, <strong>input1.txt</strong> and so on. 

This Python script will allow you to generate all the <b>output.txt</b> files, say of the form <strong>output0.txt</strong>, <strong>output1.txt</strong> and so on and also move all the input files to a folder called <strong>input</strong> and the output files to a folder called <strong>output</strong>  


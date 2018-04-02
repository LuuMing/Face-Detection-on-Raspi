num=$(cat info.txt |wc -l)
opencv_createsamples -info ./info.txt -vec ./pos.vec -num $num

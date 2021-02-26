# declare -a arr=("Google.com" "Youtube.com" "Tmall.com")
declare -a commands=("python mydig.py" "dig" "dig @8.8.8.8")
arraylength=${#commands[@]}
declare -a arr=(`cat sites.txt`)
path=(`echo $PWD`)
echo "START"
echo $path
if [ ! -d $path/result ] 
then
    mkdir $path/result
fi

for (( i=1; i<${arraylength}+1; i++ ));
do  
    echo ${commands[$i-1]} 
    echo $i
    if [ ! -d $path/result/$i ] 
    then
        mkdir $path/result/$i
    fi
    for web in "${arr[@]}"
    do
        echo $web > result/$i/$web.txt
        for t in {1..10}
        do  
            # echo $t >> result/$i/$web.txt
            ${commands[$i-1]} $web | grep time | sed 's/[^0-9]*//g'  >> result/$i/$web.txt
        done
    done
done
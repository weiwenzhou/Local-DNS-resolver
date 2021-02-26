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

for web in "${arr[@]}"
do
    echo $web > result/$web.csv
    for t in {1..10}
    do  
        for (( i=1; i<${arraylength}+1; i++ ));
        do
            ${commands[$i-1]} $web | grep time | sed 's/[^0-9]*//g' >> result/$web.csv
            truncate --size -1 result/$web.csv
            echo ',' >> result/$web.csv
            truncate --size -1 result/$web.csv
        done
        truncate --size -1 result/$web.csv
        echo '' >> result/$web.csv
    done
done
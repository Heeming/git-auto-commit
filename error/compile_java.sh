while :
do
    a=`pgrep $1`

    if [ -n "$a" ];then
        sh ./sub_compile_java.sh $1
        if [ $? -eq 0];then
            pass
        else
            e=`sh ./sub_compile_java.sh $1 2>&1 >/dev/null`
        fi
        sh ./continue.sh
        sh ./error_autoCommitProcess $e
    fi
    sleep 60
done
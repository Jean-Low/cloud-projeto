sudo apt update
sudo apt install -y python3-pip 
sudo apt install -y python3-flask
pip3 install flask
pip3 install flask_restful
FLASK_APP=rest.py flask run

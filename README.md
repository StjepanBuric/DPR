# DANAŠNJI ZADATAK

  1. podijelite se u grupe i rješavajte u grupi
  2. forkajte ovaj repozitorij
  3. klonirajte ga i instalirajte
  4. napravite *management command* koja sa stranica HNB-a poziva današnji tečaj
  5. napravite API pozive koristeći Django REST Framework Viewsets koji ispisuju listu tečajnica te, pri otvaranju pojedinačne tečajnice, ispisuju detalje
  6. pushajte to na svoj repozitorij i napravite pull request prema ovome repozitoriju
  7. najbolja grupa bira temu, ostalima ću ja zadati prema temi najbolje grupe
  
# INSTALACIJA

  pyvenv <dir>
  
  cd <dir>/
  
  . bin/activate
  
  git clone https://github.com/VSITE-python/DPR.git
  
  cd DPR/
  
  pip install -r requirements.txt 
  
  python manage.py migrate
  
  python manage.py runserver

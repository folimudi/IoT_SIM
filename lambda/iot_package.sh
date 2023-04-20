
cd /Users/juanrodriguez/Documents/GPT_Python/IoT_SIM/lib/python3.9/site-packages
zip -r ../../../../my-deployment-package.zip .
cd ../../../lambda
zip -g ../../my-deployment-package.zip lambda_function.py
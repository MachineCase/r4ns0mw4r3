import os 
import pyaes

extencao = "ps2a666"
pasta = "./arquivos"

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))
        filename = os.path.join(diretorio, arquivo)
        if(extencao in filename):
            file = open(filename, "rb")
            file_data = file.read()
            file.close()
            #Remover o arquivo
            os.remove(filename)
            #Chave de criptografia
            key = b"1234567891234567"
            aes = pyaes.AESModeOfOperationCTR(key)
            #Criptografando o arquivo
            crypto_data = aes.decrypt(file_data)
            #Salvar o arquivo criptografado
            new_file = filename.replace(extencao, "")
            new_file = open(f'{new_file}', "wb")
            new_file.write(crypto_data)
            new_file.close()

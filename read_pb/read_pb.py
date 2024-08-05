import fact_pb2

def read_protobuf_binary(file_path):
    # Cria uma instância da mensagem FactList
    fact_list = fact_pb2.FactList()
    
    # Lê o conteúdo binário do arquivo
    with open(file_path, 'rb') as f:
        fact_list.ParseFromString(f.read())
    
    # Imprime os fatos lidos
    for fact in fact_list.facts:
        print(f'ID: {fact.id}, Fact: {fact.fact}, User ID: {fact.user_id}')

if __name__ == "__main__":
    # Substitua 'joaovba' pelo caminho do seu arquivo binário
    read_protobuf_binary('joaovba')

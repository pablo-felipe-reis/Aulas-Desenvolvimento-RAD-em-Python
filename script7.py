import sqlite3 as conector
import os

print("=" * 50)
print("SCRIPT 7 - ALTERAR TABELA VEICULO")
print("=" * 50)

def alterar_tabela_veiculo():
    print("Iniciando alteracao da tabela Veiculo...")
    
    try:
        # Verificar se o banco existe
        if not os.path.exists("veiculos.db"):
            print("❌ ERRO: Arquivo veiculos.db nao encontrado!")
            return
            
        print("✅ Banco de dados encontrado")
        
        # Conectar ao banco
        conexao = conector.connect("veiculos.db")
        cursor = conexao.cursor()
        print("✅ Conectado ao banco veiculos.db")

        # Listar TODAS as tabelas para debug
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        todas_tabelas = cursor.fetchall()
        print("📋 Todas as tabelas no banco:", todas_tabelas)

        # Verificar se a tabela Veiculo existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Veiculo'")
        if not cursor.fetchone():
            print("❌ ERRO: Tabela 'Veiculo' nao existe!")
            return
            
        print("✅ Tabela Veiculo encontrada!")

        # Verificar colunas existentes
        cursor.execute("PRAGMA table_info(Veiculo)")
        colunas = [coluna[1] for coluna in cursor.fetchall()]
        print("📋 Colunas atuais:", colunas)
        
        if 'motor' in colunas:
            print("ℹ️  Coluna 'motor' ja existe na tabela Veiculo")
        else:
            # Adicionar nova coluna
            comando = "ALTER TABLE Veiculo ADD COLUMN motor REAL;"
            cursor.execute(comando)
            conexao.commit()
            print("✅ Coluna 'motor' adicionada com sucesso!")
            
            # Atualizar valores
            cursor.execute("UPDATE Veiculo SET motor = 1.0")
            conexao.commit()
            print("✅ Valores padrao definidos para motor")

        # Mostrar estrutura final
        print("\n📊 Estrutura final da tabela Veiculo:")
        cursor.execute("PRAGMA table_info(Veiculo)")
        for coluna in cursor.fetchall():
            print(f"  {coluna[1]} ({coluna[2]})")
            
        # Mostrar dados
        print("\n🚗 Veiculos cadastrados:")
        cursor.execute("SELECT * FROM Veiculo")
        for veiculo in cursor.fetchall():
            print(f"  {veiculo}")
            
    except conector.Error as erro:
        print(f"❌ Erro SQLite: {erro}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()
        print("Operacao finalizada.")

# Executar
if __name__ == "__main__":
    alterar_tabela_veiculo()

from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione_tratta import SpedizioneTratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def get_all_hub():
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM Hub """
        try:
            cursor.execute(query)
            for row in cursor:
                hub = Hub(
                    row['id'],
                    row['codice'],
                    row['nome'],
                    row['citta'],
                    row['stato'],
                    row['latitudine'],
                    row['longitudine'])
                result.append(hub)

        except Exception as e:
            print(f"Errore nel database (get_all_hub): {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()

        return result


    @staticmethod
    def get_all_tratte():
        cnx = DBConnect.get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT LEAST(id_hub_origine, id_hub_destinazione) AS hub1, GREATEST(id_hub_origine , id_hub_destinazione) AS hub2, AVG(valore_merce) AS valore_medio
                    FROM spedizione  
                    GROUP BY LEAST(id_hub_origine, id_hub_destinazione), GREATEST(id_hub_origine, id_hub_destinazione)""")
        try:
            cursor.execute(query)
            for row in cursor:
                tratta = SpedizioneTratta(
                    id_hub_origine = row['hub1'],
                    id_hub_destinazione = row['hub2'],
                    media_valore_merce = row['valore_medio'])

                result.append(tratta)

        except Exception as e:
            print(f"Errore durante la query get_tratta: {e}")
            result = None

        finally:
            cursor.close()
            cnx.close()
        return result


    # TODO


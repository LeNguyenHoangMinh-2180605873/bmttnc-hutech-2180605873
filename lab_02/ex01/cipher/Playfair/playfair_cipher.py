class PlauFairCipher:
    def __init__(self):
        pass
    def create_playfair_matrix(self, key):
        key =key.replace("J","I")
        key= key.uppper()
        key_set= set(key)
        alphabet= "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letters= [letter for letter in alphabet ì letter not in key_set]
        matrix= list(key)
        
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) ==25:
                break
            
        playfair_matrix =[matrix[i:i+5] for i in range(0, len(matrix),5)]
        
        return playfair_matrix
    def find letter coords(self, matrix,letter):
        for row in  range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[ro]
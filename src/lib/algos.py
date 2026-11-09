

class Encryption:
    def xor(text: list[int], key: list[int]) -> int:
        """Perform XOR operation between two integers.
        Args:
            text (int): The first integer.
            key (int): The second integer.
        Returns:
            int: The result of the XOR operation.
        """

        ret: str = ""
        for t, k in zip(text, key):
            ret += str(t ^ k)  # XOR演算を行い、結果を文字列として連結

        return  int(ret, 2)  # 最終的な結果を整数として返す
    

class Decryption:
    def xor(ciphertext: int, key: list[int]) -> int:
        """Decrypt a ciphertext using XOR operation with a given key.
        Args:
            ciphertext (int): The encrypted integer to be decrypted.
            key (list[int]): The key used for decryption, represented as a list of integers.
        Returns:
            int: The decrypted integer result.
        """

        # Convert the ciphertext to its binary representation and pad it to match the key length
        binary_ciphertext = bin(ciphertext)[2:].zfill(len(key))

        # Perform XOR decryption using the provided key
        decrypted_binary = ""
        for c, k in zip(binary_ciphertext, key):
            decrypted_binary += str(int(c) ^ k)  # XOR演算を行い、結果を文字列として連結

        return int(decrypted_binary, 2)  # 最終的な結果を整数として返す


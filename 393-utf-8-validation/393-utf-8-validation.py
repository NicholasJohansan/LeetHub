class Solution:
    
    def convert_to_binary(self, num):
        binary = bin(num)[2:]
        if len(binary) != 8:
            binary = ("0" * (8 - len(binary))) + binary
        return binary
    
    def count_initial_ones(self, byte):
        ones = 0
        for bit in byte:
            if bit == "1":
                ones += 1
            else:
                break
        return ones
    
    def validUtf8(self, data: List[int]) -> bool:
        byte_list = list(map(self.convert_to_binary, data))
        i = 0
        while i < len(byte_list):
            curr_byte = byte_list[i]
            curr_ones = self.count_initial_ones(curr_byte)
            if curr_ones == 0:
                i += 1
                continue
            elif curr_ones >= 2 and curr_ones <= 4:
                char_bytes = curr_ones
                if i + (char_bytes - 1) > len(byte_list):
                    return False
                for j in range(i + 1, i + char_bytes):
                    consec_byte = byte_list[j]
                    consec_ones = self.count_initial_ones(consec_byte)
                    if consec_ones != 1:
                        return False
                i += char_bytes
            else:
                return False
                
        return True
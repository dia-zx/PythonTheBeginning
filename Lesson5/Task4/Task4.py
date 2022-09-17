# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# метод для сжатия последовательности байт данных {data} путем поиска повторяющихся сэмплов размером 1..4 байта
# метод кода: {байт - служебный; последовательность данных [n байт] ...байт - служебный; последовательность данных [n байт]}
# служебный байт содержит:
#       информацию о длине байт данных, либо количество повторяющихся последовательностей (первые 5 либо 7 бит)
#       информацию о типе данных (последние 3 бита):
#               b000N_NNN - последовательность размером 1 байт, число повторов : '..N_NNN'
#               b001N_NNN - последовательность размером 2 байт, число повторов : '..N_NNN'
#               b010N_NNN - последовательность размером 3 байт, число повторов : '..N_NNN'
#               b011N_NNN - последовательность размером 4 байт, число повторов : '..N_NNN'
#               b1NNN_NNN - последовательность отсутствует, далее идет блок данных, длиной '..NNN_NNN'
def compress(data: bytes):
    res = bytearray()
    startpos = 0
    curpos = startpos
    while True:
        # с позиции curpos пробежимся в поисках повторяющихся последовательностей из 1, 2, 3, 4 байт
        sample_res = []
        for sample_length in range(1, 5):
            sample_res.append(FindSamples(sample_length, data[curpos::]))

        # из результатов поиска последовательностей найдем наиболее результативную
        max_index_compress = -1
        max_compress = -1
        for i in range(0, 4):
            if sample_res[i][1] == 0:  # нет сжатия
                continue
            if max_compress < sample_res[i][0]:
                max_compress = sample_res[i][0]
                max_index_compress = i

        if max_compress > 0:  # если есть результативная последовательность!
            if curpos != startpos:  # добавим несжатые байты
                res.extend(bytes([(1 << 7) | (curpos - startpos)]) + data[startpos: curpos])
            res.extend(sample_res[max_index_compress][2])  # добавляем код нашей последовательности
            startpos = curpos + sample_res[max_index_compress][1]  # сдвигаем начальную и текущую позицию
            curpos = startpos
        else:
            curpos += 1  # увеличиваем позицию
        if curpos - startpos == 0b01111111 or curpos == len(data) and startpos != len(data):
            res.extend(bytes([(1 << 7) | (curpos - startpos)]) + data[startpos: curpos])
            startpos = curpos
        if curpos >= len(data):
            return res

#поиск повторяющихся последовательностей 1..4 байт
# sample_length - размер последовательности
# data - массив данных
def FindSamples(sample_length: int, data: bytes):
    count = 0
    cur_pos = 0
    while cur_pos + sample_length <= len(data):
        if data[0: sample_length] != data[cur_pos: cur_pos + sample_length]:
            break
        count += 1
        cur_pos += sample_length
        if count == 0b00011111:
            break
    length_bytes = count * sample_length  # размер [байт] исходного блока (без сжатия)
    compressed_bytes = length_bytes - (1 + sample_length)  # число 'сжатых' байт
    compressed_data = bytes()  # результат сжатия
    if count:
        compressed_data = bytes([((sample_length - 1) << 5) | count]) + data[0:sample_length]
    return [compressed_bytes, length_bytes, compressed_data]


# метод распаковки данных.
# метод не содержит проверок на соответствие данных. Считаем данные корректны и получены методом compress()
def decompress(data: bytes):
    res = bytearray()
    curpos = 0
    while curpos < len(data):
        if data[
            curpos] & 0b10000000:  # b1NNN_NNN - последовательность отсутствует, далее идет блок данных, длиной '..NNN_NNN'
            n = data[curpos] & 0b01111111
            res.extend(data[curpos + 1: curpos + 1 + n])
            curpos += 1 + n
            continue
        n = data[curpos] & 0b00011111  # число повторов
        size = (data[curpos] >> 5) + 1  # размер последовательности 1..4 байт
        for i in range(0, n):
            res.extend(data[curpos + 1: curpos + 1 + size])
        curpos += 1 + size
    return res


data = bytes()
with open("SomeText.txt", "rb") as f:
    data = f.read()

with open("Compressed.dat", "wb") as f:
    f.write(compress(data))

with open("Compressed.dat", "rb") as f:
    data = f.read()

with open("DeCompressed.txt", "wb") as f:
    f.write(decompress(data))

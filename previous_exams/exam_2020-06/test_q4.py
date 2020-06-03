# Tests
message = 'Robber Bob robs ten banks'
print('Original message:',  message)

# Part A
pcrypto = PirateLanguage()
psecret = pcrypto.encode(message)
print('Pirate encrypted:', psecret)
assert pcrypto.decode(psecret) == message # Decoding should give us back the original message

# Part C
# Check shift helper works correctly
assert Rotator.shift('a', 1) == 'b' # a+1 should become b
assert Rotator.shift('a', -1) == 'z' # a-1 should become z
assert Rotator.shift('g', 13) == 't' # g+13 should become t
assert Rotator.shift(' ', 13) == ' ' # characters not present in the english alphabet are not replaced.

rotcrypto = Rotator(13)
rotsecret = rotcrypto.encode(message)
print('Rotate encrypted:', rotsecret)
assert rotcrypto.decode(rotsecret) == message # Decoding should give us back the original message

# Part D
repcrypto = Replacer({x:y for x,y in zip('abcdefghijklmnopqrstuvwxyz', 'kfghiwxucdyzlmveqabpnojrst')})
repsecret = repcrypto.encode(message)
print('Replace encrypted:', repsecret)
assert repcrypto.decode(repsecret) == message # Decoding should give us back the original message

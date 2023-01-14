
def std(nums):
    n = len(nums)
    avg = sum(nums) / n
    return (sum(map(lambda e: (e - avg) * (e - avg), nums)) / n) ** 0.5

if __name__ == '__main__':
    Hausdoff_nums = [5.0,
3.605551275463989,
6.48074069840786,
4.69041575982343,
4.58257569495584,
3.3166247903554,
5.0990195135927845,
6.928203230275509,
3.872983346207417,
7.0710678118654755,
4.0,
3.7416573867739413,
4.358898943540674,
6.708203932499369,
3.605551275463989,
4.123105625617661,
6.244997998398398,
4.795831523312719,
2.6457513110645907,
4.47213595499958,
4.795831523312719,
5.0,
4.242640687119285,
4.47213595499958,
3.1622776601683795,
5.196152422706632,
4.69041575982343,
4.47213595499958,
5.196152422706632,
4.795831523312719,
4.358898943540674,
6.928203230275509,
5.291502622129181,
3.605551275463989,
7.416198487095663,
4.47213595499958,
5.656854249492381,
6.164414002968976,
4.69041575982343,
4.58257569495584,
6.855654600401044,
4.47213595499958,
4.795831523312719,
6.928203230275509,
5.385164807134504,
4.58257569495584,
5.0,
7.3484692283495345,
3.1622776601683795,
4.242640687119285,
5.5677643628300215,
2.8284271247461903,
4.47213595499958,
5.0,
6.164414002968976,
4.123105625617661,
6.0,
4.58257569495584,
3.4641016151377544,
3.605551275463989,
6.244997998398398,
7.483314773547883,
8.426149773176359,
3.872983346207417,
3.4641016151377544,
6.164414002968976,
7.14142842854285,
6.0,
3.605551275463989,
3.0,
6.855654600401044,
4.0,
5.830951894845301,
5.196152422706632,
5.744562646538029,
6.164414002968976,
4.898979485566356,
3.7416573867739413,
5.0,
3.872983346207417,
3.7416573867739413,
4.69041575982343,
3.872983346207417,
5.744562646538029,
4.242640687119285,
4.358898943540674,
4.58257569495584,
6.48074069840786,
4.898979485566356,
3.3166247903554,
5.0,
3.605551275463989,
7.0,
5.0990195135927845,
3.605551275463989,
4.0,
4.358898943540674,
6.082762530298219,
5.5677643628300215,
7.3484692283495345]
    print('Hausdoff Standard Deviation:',std(Hausdoff_nums))

    MAD_nums = [1.0415557835350162,
1.180346859701717,
1.7058946966178548,
1.1923471475079002,
1.1292766652124213,
0.6682620977991249,
1.154338755069823,
1.3657570693761714,
1.8702506310508258,
1.6668383274543963,
1.5677539184796179,
1.0207978435911664,
0.8811831939359737,
1.6852165873025307,
1.1618624636256825,
0.9409039324805103,
1.4451989468900757,
1.1264625023858101,
0.6103655937573887,
1.5118830921698954,
1.0430655313092565,
0.7629277350568655,
2.0053599679593126,
1.9231311781799547,
1.5981060963772764,
2.2851412768915895,
1.0832753967021729,
0.7267050234908584,
1.1635477072794955,
1.0167620917078295,
1.1283074965650406,
1.4690228546305288,
1.5230113010482094,
1.7089534964762696,
0.9798997441642154,
1.3902349390711637,
1.8036368605037716,
1.7289790852017237,
1.5362780937736766,
0.9115115991129875,
1.370827602401949,
1.0660451132873796,
1.2267401741781232,
1.0915047859371074,
1.6601863885073818,
0.8136290280655399,
1.0279854932207377,
2.408159684748318,
0.8982100396730897,
1.073930381295658,
1.6724524938191707,
0.9903491483224012,
1.2862681000631722,
0.8696694835791464,
2.0900149577469804,
1.4271949421886525,
1.6001697010808456,
1.4425379651469714,
1.5056670286305436,
1.4152777403105516,
0.9535895197464492,
0.7280746911638369,
2.476067380296162,
1.3299885622109748,
1.3978060364384692,
1.7890693493585996,
1.96340972847291,
2.2396949128220625,
1.1715565479033563,
0.9588511707456622,
1.1448298405984152,
1.0094396598593196,
2.4378125802675576,
1.7093287881975197,
2.816636649336494,
0.8435888853357028,
1.3598973743747738,
1.300815284680117,
2.2207571191521995,
1.2556374150660075,
1.5631725883942362,
0.5806368277446864,
1.6490882624843919,
2.3908556522460582,
0.9341420159810253,
1.2121286161360942,
1.407328503162504,
1.1077220610011949,
1.3552985199294763,
1.5350974728322755,
1.4292581147767773,
1.0849889464150015,
1.1064349525313113,
1.4945842170693222,
1.4602993503543502,
1.3709942974691478,
0.8189155466354813,
1.122309377930608,
1.4865418002792143,
1.103272592382126]
    print('MAD Standard Deviation:',std(MAD_nums))
    dice_nums = [0.9664,
0.9375,
0.9022,
0.8379,
0.8819,
0.9387,
0.8902,
0.9477,
0.9476,
0.9394,
0.9436,
0.9629,
0.9287,
0.9355,
0.9673,
0.9658,
0.9124,
0.9375,
0.9635,
0.9272,
0.9610,
0.9657,
0.9460,
0.9187,
0.9518,
0.9555,
0.9298,
0.9736,
0.9581,
0.9576,
0.9111,
0.9080,
0.9200,
0.9483,
0.9368,
0.9489,
0.8955,
0.8991,
0.9325,
0.9368,
0.9480,
0.9433,
0.9495,
0.9556,
0.9341,
0.9708,
0.9141,
0.9380,
0.9613,
0.9629,
0.9580,
0.9704,
0.9146,
0.9317,
0.9523,
0.9256,
0.9663,
0.9532,
0.9640,
0.9614,
0.9563,
0.9549,
0.8519,
0.9427,
0.9186,
0.8155,
0.9294,
0.9598,
0.9642,
0.9810,
0.9340,
0.9338,
0.8892,
0.9646,
0.9108,
0.9637,
0.9499,
0.9698,
0.9526,
0.9737,
0.9519,
0.9681,
0.9602,
0.8872,
0.9356,
0.8837,
0.9545,
0.9621,
0.9424,
0.9218,
0.9063,
0.9184,
0.9437,
0.9323,
0.9540,
0.9452,
0.9533,
0.7310,
0.9628,
0.9476]
    print('dice Standard Deviation:',std(dice_nums))
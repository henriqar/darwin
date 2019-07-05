
import htcondor
import classad

import collections
import time

# sub = htcondor.Submit({
#     'executable':'/bin/sleep',
#     'arguments':'1m',
#     'initialdir':'/home/henrique.rusa/projects/darwin/tests'})

sub = htcondor.Submit({
    'executable':'/bin/sleep',
    'arguments':'1m',
    'error':'err.$(ClusterId)',
    'output':'out.$(ClusterId)'})

schedd = htcondor.Schedd()
with schedd.transaction() as txn:
    cid1 = sub.queue(txn)
    print(cid1)

with schedd.transaction() as txn:
    cid2 = sub.queue(txn)
    print(cid2)


jl = collections.deque([cid1, cid2])

j = schedd.xquery( requirements='(ClusterId == {}) || (ClusterId == {})'.format(cid1, cid2), projection=['ClusterId', 'JobStatus'])

print('try of multiple job xquery:')
for j in j:
    print('jobn: ' + str(j))

while jl:

    item = jl.popleft()
    j = schedd.xquery( requirements='(ClusterId == {}) || (ClusterId == {})'.format(item), projection=['ClusterId', 'JobStatus'])

    try:
        a = next(j)
        jl.append(item)
    except StopIteration:
        print('job {} ended'.format(item))

    print('tried {} but it has status {}'.format(cid1, a.get('JobStatus')))
    time.sleep(10)


    print('->: ' + str(a.get('ClusterId')))
    print('->: ' + str(a.get('JobStatus')))



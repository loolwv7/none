= btrfs how to =
== I get "No space left on device" errors, but df says I've got lots of space ==
{{{
 btrfs fi show
Label: 'ROOT'  uuid: be9d27e5-ce19-4c33-b45a-e8b459b5ebcb
        Total devices 1 FS bytes used 12.71GiB
        devid    1 size 16.30GiB used 16.30GiB path /dev/sda2

Label: none  uuid: 1f61af11-61b2-41fa-be89-fcd39cae6e6c
        Total devices 1 FS bytes used 63.77GiB
        devid    1 size 70.00GiB used 70.00GiB path /dev/sda3

Btrfs v3.14.2
}}}

btrfs fi df /
}}}
Data, single: total=15.01GiB, used=11.73GiB
System, single: total=4.00MiB, used=16.00KiB
Metadata, single: total=1.28GiB, used=1003.56MiB
unknown, single: total=288.00MiB, used=0.00
}}}
 * Note that the Metadata used value is fairly close (75% or more) to the Metadata
total value, but there's lots of Data space left.

{{{
# btrfs fi balance start -dusage=5 -v / 
Dumping filters: flags 0x1, state 0x0, force is off
  DATA (flags 0x2): balancing, usage=5
Done, had to relocate 0 out of 24 chunks
}}}
 * tail /var/log/messages will print:
{{{
[  449.306097] BTRFS info (device sda2): relocating block group 17469276160 flags 4
[  469.507692] BTRFS info (device sda2): relocating block group 17469276160 flags 4
[  531.880157] BTRFS info (device sda2): relocating block group 17469276160 flags 4
[  555.834059] BTRFS info (device sda2): relocating block group 17469276160 flags 4
[  578.916511] BTRFS info (device sda2): relocating block group 12582912 flags 1
[  579.298839] BTRFS info (device sda2): found 158 extents
[  580.045425] BTRFS info (device sda2): found 158 extents
}}}

Note that there should be no space between the -d and the usage. This command
will attempt to relocate data in empty or near-empty data chunks (at most 5% used, in this example), allowing the space to be reclaimed and
reassigned to metadata.

If the balance command ends with "Done, had to relocate 0 out of XX chunks",
then you need to increase the "dusage" percentage parameter till at least one chunk is relocated.


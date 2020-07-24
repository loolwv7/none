= PASS password managerment =
== initialize password store ==
{{{
$ pass init "Merlyn Password Storage Key"
mkdir: created directory ‘/home/merlyn/.password-store/’
Password store initialized for Merlyn Password Storage Key

}}}

== create GPG key ==
{{{
$ gpg --list-keys
 /home/merlyn/.gnupg/pubring.gpg
 -------------------------------
 pub   2048R/8D75B716 2011-04-21 [expired: 2012-04-20]
 uid       [ expired] merlyn ([][]) <loolwv7@gmail.com>

 pub   2048R/74D27AA9 2013-07-01
 uid       [ultimate] merlyn <loolwv7@gmail.com>
 sub   2048R/32522BF9 2013-07-01


$ pass init 74D27AA9
Password store initialized for 74D27AA9
[main 6f5097d] Set GPG id to 74D27AA9.
1 file changed, 1 insertion(+), 1 deletion(-)

$ gpg --edit-key 74D27AA9
}}}

== Generate new password ==
{{{
$ pass generate -c Gmail/loolwv7 16
 An entry already exists for Gmail. Overwrite it? [y/N] y
 Copied Gmail to clipboard. Will clear in 45 seconds.
}}}

== Copy existing password to clipboard ==
{{{
$ pass -c Gmail/loolwv7
Copied Gmail/loolwv7 to clipboard. Will clear in 45 seconds.
}}}

== Add password to store ==
{{{
pass insert Shopping/wiggle.com/loolwv7@gmail.com
}}}

== Find existing passwords in store that match .com ==
{{{
pass find lool 
}}

== Version control ==

To keep historical passwords, including deleted ones if we find we do need them
again one day, we can set up some automatic version control on the directory
with pass git init:
{{{
$ pass git init
Reinitialized existing Git repository in /home/merlyn/.password-store/.git/

$ pass insert Gmail/bbbcccbobobo@gmail.com
Enter password for Gmail/bbbcccbobobo@gmail.com: 
Retype password for Gmail/bbbcccbobobo@gmail.com: 
[main cf17704] Add given password for Gmail/bbbcccbobobo@gmail.com to store.
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 Gmail/bbbcccbobobo@gmail.com.gpg

}}}

== git remote store ==
{{{
pass git remote add origin https://github.com/loolwv7/private.git
pass git push
 Everything up-to-date
}}}

== BACKUP !!! ==
Because the password files are all encrypted only to your GnuPG key, you can
relatively safely back up the store on remote and third-party sites simply by
copying the ~/.password-store directory. If the filenames themselves contain
sensitive information, such as private usernames or sites, you might like to
back up an encrypted tarball of the store instead:

{{{
$ tar -cz .password-store | gpg --sign --encrypt -r 0x77BB8872 > password-store-backup.tar.gz.gpg
}}}

This directory can be restored in a similar way:
{{{
$ gpg --decrypt \
< password-store-backup.tar.gz.gpg \
| tar -xz 
}}}


== Troubleshooting ==

{{{
$ pass generate mail.google.com 15
gpg: Merlyn Password Storage Key: skipped: No public key
gpg: [stdin]: encryption failed: No public key
fatal: pathspec '/home/merlyn/.password-store/mail.google.com.gpg' did not
match any files
The generated password for mail.google.com is:
c0^(k7xlUJ;K2{m
}}}


=== if gpg --gen-key hangs ===
{{{
# emerge -av sys-apps/rng-tools
# rngd -r /dev/urandom
$ gpg --gen-key
gpg (GnuPG) 2.0.26; Copyright (C) 2013 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: Merlyn
Email address: loolwv7@gmail.com
Comment: Merlyn's
You selected this USER-ID:
    "Merlyn (Merlyn's) <loolwv7@gmail.com>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.


We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 454FD73A marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   2048R/454FD73A 2015-06-11
      Key fingerprint = D6BC 3432 8865 9947 8B59  0493 DA79 3B5F 454F D73A
uid       [ultimate] Merlyn (Merlyn's) <loolwv7@gmail.com>
sub   2048R/0CCE6BA9 2015-06-11
}}}


=== 创建“撤回”证书 ===
{{{
$ gpg --output revoke.asc --gen-revoke 454FD73A

sec  2048R/454FD73A 2015-06-11 Merlyn (Merlyn's) <loolwv7@gmail.com>

Create a revocation certificate for this key? (y/N) y
Please select the reason for the revocation:
  0 = No reason specified
  1 = Key has been compromised
  2 = Key is superseded
  3 = Key is no longer used
  Q = Cancel
(Probably you want to select 1 here)
Your decision? 1
Enter an optional description; end it with an empty line:
> Someone cracked me and got my key and passphrase
> 
Reason for revocation: Key has been compromised
Someone cracked me and got my key and passphrase
Is this okay? (y/N) y

You need a passphrase to unlock the secret key for
user: "Merlyn (Merlyn's) <loolwv7@gmail.com>"
2048-bit RSA key, ID 454FD73A, created 2015-06-11

gpg: Invalid passphrase; please try again ...

You need a passphrase to unlock the secret key for
user: "Merlyn (Merlyn's) <loolwv7@gmail.com>"
2048-bit RSA key, ID 454FD73A, created 2015-06-11

ASCII armored output forced.
Revocation certificate created.

Please move it to a medium which you can hide away; if Mallory gets
access to this certificate he can use it to make your key unusable.
It is smart to print this certificate and store it away, just in case
your media become unreadable.  But have some caution:  The print system of
your machine might store the data and make it available to others!

}}}



http://unix.stackexchange.com/questions/53912/i-try-to-add-passwords-to-the-pass-password-manager-but-my-attempts-fail-with

http://www.stackednotion.com/blog/2012/09/10/setting-up-pass-on-os-x/

http://blog.sanctum.geek.nz/linux-crypto-passwords/

http://stackoverflow.com/questions/24114676/git-error-failed-to-push-some-refs-to

# Bootcamp Santander 2025 / Trilha Back-End com Python

A página principal do bootcamp está hospedada no [dio.me](https://web.dio.me/track/santander-2025-python-back-end)

## Curso Versionamento de Código com Git e GitHub / Módulo 1

🏫 Nível básico
</br>
⏳ Duração 2 hrs

Para [continuar o curso](https://web.dio.me/track/santander-2025-python-back-end/course/versionamento-de-codigo-com-git-e-github/learning/f3cbaa66-efbd-4c25-842e-2069c188c066?autoplay=1)

### Git local configuration

#### Username and email for commits

`git config --global user.name "Filipe Bezerra"`
</br>
`git config --global user.email filipebzerra@gmail.com`

#### Main branch naming convention

`git config --global init.defaultbranch main`

### GitHub authentication

#### Generate a SSH Key

`ssh-keygen -t ed25519 -C "filipebzerra@gmail.com"`

#### Start SSH agent

`eval "$(ssh-agent -s)"`

#### Add SSH key to the agent

`ssh-add --apple-use-keychain ~/.ssh/id_ed25519`

#### Check git config file

`open ~/.ssh/config`

Check its contents if contains exactly the following lines:

```config
Host *.github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

#### Copy SSH key contents and add to GitHub

`pbcopy < ~/.ssh/id_ed25519.pub`

#### You can check your access to GitHub

`ssh -T <git@github.com>`

#### Extra: Store git credentials

`git config --global credential.helper store`

Validate this configuration with

`git config --global --show-origin credential.helper`

You can check for more info:

- <https://git-scm.com/docs/git-credential-store>
- <https://git-scm.com/docs/gitcredentials>
- <https://git-scm.com/book/pt-br/v2/Git-Tools-Credential-Storage>

### Common Git commands

#### Initialize repository

`git init`

#### Add single file

`git add README.md`

#### Add all files

`git add .`

#### Save changes locally

`git commit -m "This is a commit"`

#### Force branch to rename

`git branch -M main`

#### Add remote repo

`git remote add origin https://github.com/filipebezerra/santander-2025-python-back-end.git`

#### Send local changes to remote repo

`git push -u origin main`

#### Clone repository locally

`git clone https://github.com/filipebezerra/santander-2025-python-back-end.git`

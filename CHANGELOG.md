# CHANGELOG

<!-- version list -->

## v0.13.3 (2026-04-20)

### Bug Fixes

- Improve gitlab release ci
  ([`1ee4ad9`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1ee4ad9d05b2d2635d6fb3cf6aeea71dfb9416a7))


## v0.13.2 (2026-04-20)

### Bug Fixes

- Gitlab release needs personal/project token
  ([`094b745`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/094b74569f8ba131fae5a798df8979ad63908142))


## v0.13.1 (2026-04-20)

### Bug Fixes

- Gitlab release needs releases api
  ([`d071203`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/d0712032e562178aea6eb1eaf42591978c69e873))


## v0.13.0 (2026-04-20)

### Bug Fixes

- Gitlab release needs checkout
  ([`31fb57d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/31fb57d378fe6dc968ac0bbb9448d2607b55ea47))

- **deps**: Update dependency copier to v9.14.2
  ([`af17c0d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/af17c0db26ed7fedf36c72fd7c2188dd575621c0))

- **deps**: Update dependency copier to v9.14.3
  ([`57c45c2`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/57c45c22f11f5eb7cef7d34d54d317e724d2730c))

### Features

- Add automated release
  ([`9d50c88`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/9d50c887343cd94a0d8b3dedd6a74b6c53bc2e5c))


## v0.12.1 (2026-04-05)

### Bug Fixes

- Avoid passing release CLI_ARGS to pre-release-checks
  ([`c19313b`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/c19313bc5f06345cbdef3b883f669d1def0f3fb7))

### Documentation

- Add non-interactive usage notes to README for agents and CI
  ([`504df1a`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/504df1a0df21d1624bf474dc7beedcc7c75ad109))

### Testing

- Assert structured file content instead of raw substrings
  ([`1378d50`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1378d50d98dd549f0005e8f1aa57fdd2bdd4646c))


## v0.12.0 (2026-04-05)

### Bug Fixes

- **renovate**: Track _min_copier_version in copier.yml.tmpl files
  ([`a73f935`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a73f935c29bee44002bb878760c83504ffb2afde))

### Features

- Add min_python_version question
  ([`418cbe1`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/418cbe1da240c26b52254b891fee63268406a9e1))

- Add sub_project_factory fixture
  ([`e3af541`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/e3af54197bdf913bab4d4e9b9660bbeed442fcc2))


## v0.11.0 (2026-04-03)

### Features

- Release improvements
  ([`b21d2a4`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/b21d2a4489923d8d2fa29cf3e3f0bb64e4d64f69))


## v0.10.0 (2026-04-03)

### Bug Fixes

- Unpin docker image
  ([`0c20c49`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0c20c49ba1c4a10df2c4f177b0cf5b6dd625bdc0))

### Features

- Gitlab CI improvements
  ([`6e17f73`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/6e17f731130605123f4567283f46f0113224bb45))


## v0.9.0 (2026-04-03)

### Documentation

- Improve README
  ([`4a6e029`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/4a6e0293d0b5d42dbb8e953866f6daabc527cc41))

- Improve test harness docs
  ([`5ed4694`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5ed469427d97763cc367d2ae6a834b0665a63b7c))

- Improve test harness docs
  ([`d8839a5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/d8839a573b3db3236c950652ae8544b6d8b573c3))

- Improve test suite docs
  ([`e672840`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/e672840fb59855df518d6cecf235bcaf92fac051))

### Features

- Improve template inspection commands
  ([`d738a9a`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/d738a9a19f6b3b238f0543e0ad8f460093c1e01b))

- Update CI choices
  ([`5898c5f`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5898c5f5272fa2a3d2e9831202f38bac25cd7815))


## v0.8.1 (2026-04-01)

### Bug Fixes

- Correct test
  ([`fa6ca07`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/fa6ca07129140e2f15a9b6667a65fc5201126624))

### Features

- Add no-default answer handling to tests
  ([`a395bf4`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a395bf4add207a1570fa76a5f8641133921e49a1))


## v0.8.0 (2026-04-01)

### Bug Fixes

- Correct prek usage
  ([`761dca6`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/761dca6db4f713ce3b086192955dcb5ffd430bb5))

### Features

- Experimental switch to prek from pre-commit
  ([`a283602`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a283602395ea1c3b0ded234ac744d3c52527fc8b))

- Git fetch after release
  ([`95119f2`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/95119f263e635ac3397e3255bcc394f0520a2d2d))


## v0.7.1 (2026-03-31)

### Bug Fixes

- **deps**: Update dependency copier to v9.14.1
  ([`1d21902`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1d2190214554cdf8da2ed68c08da33077f2779b4))

### Features

- Ensure renovate updates copier and _min_copier_version in sync
  ([`1a5aa68`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1a5aa687b0894fda61e4b13378206110ed63cb12))

- **repo**: Update copier and _min_copier_version in sync
  ([`424876d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/424876d59e05fbb9cc9ee2fb56c8d09ef3ec6659))


## v0.7.0 (2026-03-30)

### Features

- Simplify test helpers
  ([`ed5f4f3`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/ed5f4f3df3da3383182e911f490812567fa07aa0))

### Testing

- Check shipped tests pass w/dirty git
  ([`a0c3921`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a0c39210b3675533e777b21b277ce52c189f23a8))


## v0.6.5 (2026-03-29)

### Features

- Add doc for Copier Template Extensions
  ([`3146091`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/3146091024b043bd1bc473be5d6017ec1bbf815b))


## v0.6.4 (2026-03-29)

### Features

- Add asciinema demo to README
  ([`5be6554`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5be6554a08b533939b74ba8fd15ff625a200cd88))

- Add placeholder asciinema demo
  ([`0bbae39`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0bbae390f4036a2bce7522f06ada7a0ef94a3df7))

- Add pydantic validated answer example
  ([`909cc3b`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/909cc3ba246ae3f3f0d9aefe7ff736a33afb02f9))


## v0.6.3 (2026-03-29)

### Features

- Add asciinema task
  ([`a1b4e5c`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a1b4e5caa7cf2ff88114a58590c93e59d30eddd5))

- Align uv version used in github ci
  ([`4f61b10`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/4f61b1013a89501aa9211b514d7166db687890c7))

- Improve docs
  ([`5145106`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5145106ca0991ad224140d0b1338a18f4692b960))

- Rename template dir for clarity
  ([`a9de300`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a9de3000a70a01398e6a282c9c781623401176d9))

- **repo**: Improve cog file updating
  ([`8389c59`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/8389c59ff13afae30ddfd68c5ea8cabdf56135ce))


## v0.6.2 (2026-03-24)

### Bug Fixes

- Correct answerfile in README
  ([`421ebd3`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/421ebd38cfd36adef22e2a1b133afae93be0696b))


## v0.6.1 (2026-03-24)

### Bug Fixes

- Correct answerfile in README
  ([`0c99142`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0c99142cfed90809db63e2adfb57cefdf44ab849))


## v0.6.0 (2026-03-24)

### Bug Fixes

- Exclude chore commits from changelog
  ([`fe2d1be`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/fe2d1be6cc1545c273a1b5a5b8f78b9e3972dcf4))

### Features

- Add release:test for local side affects test
  ([`543d2c1`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/543d2c1ba501f0f38ee39e2121a9f128a1e00b36))

- Exclude chore commits from changelog
  ([`688ebd9`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/688ebd9b2b1b01bdacc277fbf3836d1d56e101f0))

- Handle semantic release as dev dep
  ([`66dc46e`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/66dc46e7b2c04ca8bfc548a440c879e3e49f0867))

- Renovate automerges github action digest updates
  ([`029343e`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/029343e53c755a2e2d7ae2ddc979ea305922e9de))

- Update readme
  ([`0bdbdcc`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0bdbdcc885e72caad455af7252f3f962b41a48fe))


## v0.5.8 (2026-02-14)

### Chores

- **deps**: Lock file maintenance
  ([`377e2b2`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/377e2b2fd62bd5ec0e60bf9413a4f0db0800e79c))

- **deps**: Update dependency astral-sh/uv to v0.10.0
  ([`f8a896b`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f8a896b28a5046208cad39dd5357c45c3423713a))

- **deps**: Update dependency astral-sh/uv to v0.10.1
  ([`2629022`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2629022b7ddf8057b514ddaa6d75c13c77816d2d))

- **deps**: Update dependency astral-sh/uv to v0.10.2
  ([`23fb420`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/23fb42045077a38ba7c1b636c00551a6665212b9))

- **deps**: Update dependency astral-sh/uv to v0.9.30
  ([`4de339d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/4de339dc6bed1086a62ad1819c38f9eb021e4e30))

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.5.7
  ([`2b09a4a`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2b09a4aab4d83c97063a740cba98dc7f8a8054b9))

- **deps**: Update dependency git@gitlab.com:browniantech/pre-commit-copier-template.git to v0.5.5
  ([`a7dd18f`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a7dd18f3e1ab650b4559f363018d12d7c301fcbb))

- **deps**: Update docker docker tag to v29.2.1
  ([`65c19f2`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/65c19f246a683ac781ca93adb1adbac647528b42))

- **deps**: Update python:3.14-slim docker digest to 486b809
  ([`0ce52ad`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0ce52add50c27f59d354caa23f4e8f804cf2b25f))

- **deps**: Update python:3.14-slim docker digest to fa0acdc
  ([`ae975cf`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/ae975cf21fa8b1b386cc657d18d08beb2cae9da7))

### Features

- Add plumbum test example
  ([`8ea69c9`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/8ea69c94835103de60d57e472bcaefa461558c9e))

- **repo**: Add cog setup for updating gitignore
  ([`2761680`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/27616805d28bae40f59fd34e75e5857b80be5e7a))

- **repo**: Update cog setup
  ([`4aecfb0`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/4aecfb052d5b012a24e9ff3701688cbd91a111de))


## v0.5.7 (2026-02-04)

### Chores

- **deps**: Lock file maintenance
  ([`ce48b2c`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/ce48b2ce4c0700a5d17a74170d9cc4e49797e565))

- **deps**: Update debian:trixie-slim docker digest to bfc1a09
  ([`81d70d4`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/81d70d417d6048bcf904ac13ac64217b2d6cbd95))

- **deps**: Update debian:trixie-slim docker digest to f6e2cfa
  ([`dac8d92`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/dac8d92e12984bd62b592aaab7c1d34e5dea7c02))

- **deps**: Update dependency astral-sh/uv to v0.9.29
  ([`94804ad`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/94804ad0f9db0d63613793109f69e4d680b5255f))

- **deps**: Update python:3.14-slim docker digest to 0c6bb25
  ([`de87b4a`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/de87b4ab1f6a94efe3539c3d084277008948c2d7))

- **deps**: Update python:3.14-slim docker digest to 1a3c6db
  ([`f7a7142`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f7a71428bd3e718c84611da4e33502675582cbc1))

- **deps**: Update python:3.14-slim docker digest to d517cd3
  ([`241f6e6`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/241f6e64424380fd6b8c460012a9482aeb13e6d9))

- **repo**: Update copier template
  ([`d82fa18`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/d82fa181676b55b1746537781e24ab183c207662))

### Features

- Add gitlab support
  ([`8eb7896`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/8eb78965a67ebd2d7baf58fadab99a1c40c9b95c))

- Add python version matrix testing
  ([`822f4c5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/822f4c5a0a36265169578112a2ade81f37a19339))

- Relax python min version
  ([`adb1e81`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/adb1e818faf5a51560c028be34461cf692f18b29))


## v0.5.6 (2026-02-01)

### Bug Fixes

- Remove default copyright name
  ([`774d04c`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/774d04c7bc66a4e76dbeb9e8bef631c53c1d90eb))


## v0.5.5 (2026-02-01)

### Chores

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.5.4
  ([`c8fe752`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/c8fe7525d1c2c8d82b61906ed97647f1795740f4))

- **repo**: Update TODO list
  ([`3db9599`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/3db9599deb601ea6fd419116e0ecdea223b4e6e3))

### Features

- Add license choice
  ([`5b43215`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5b4321588bd8df0a3f3980df3270f43d65ca0473))

- **repo**: Refactor tests
  ([`6bb43cd`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/6bb43cd303eba2c1ce3f0c52270d8aa9e400e6e8))


## v0.5.4 (2026-02-01)

### Chores

- Improve whitespace in README
  ([`91757c5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/91757c56aafdf7bb47e16b3928e9d4bb70129cf3))


## v0.5.3 (2026-01-31)

### Chores

- Improve readme for extensions
  ([`187f39c`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/187f39c5adc8d3e731cd3c057224a3c94e2960cb))

- Update TODO list
  ([`db42bcb`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/db42bcbed4f6bd729b224870216486b0304eded9))


## v0.5.2 (2026-01-31)

### Chores

- Update copier template
  ([`f8a8c73`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f8a8c7394a597d0e61eae56fb16c8c0349bd3d92))

- Update copier template
  ([`2d97a6b`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2d97a6bbb9c985415c72c774bb405694394b2bed))

### Features

- Add support for recommended extensions
  ([`1d9fce0`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1d9fce076413e7e9733840f491a213771be4baac))


## v0.5.1 (2026-01-31)

### Chores

- **deps**: Update dependency astral-sh/uv to v0.9.28
  ([`b605025`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/b605025fadbbd74e0c0ac9ddd64174f7e9cb4e2a))

- **repo**: Update TODO list
  ([`ff41b42`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/ff41b42642eb295c81a394f8f041f9e635096f2e))


## v0.5.0 (2026-01-28)

### Chores

- **deps**: Update dependency astral-sh/uv to v0.9.27
  ([`f16229b`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f16229bac8b3913eb22060b8bf3b8813437a9781))

- **deps**: Update dependency copier to v9.11.3
  ([`3ccb4a9`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/3ccb4a9de682c0100ce7466e3536f16dc9a33eca))

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.4.1
  ([`5ab1b40`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5ab1b40ac71e0095930122075d82865deb20b942))

- **deps**: Update docker docker tag to v29.2.0
  ([`9480fc4`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/9480fc4386f7e1a67b6b39e7c6f7a0bc58a79719))

- **deps**: Update docker:29.2.0-dind docker digest to a284d31
  ([`60440f4`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/60440f48f41c2ff38b373215897cf58248e3d22a))

- **deps**: Update docker:29.2.0-dind docker digest to dbd6a47
  ([`2233b63`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2233b632613461c8ef1aa18a9acde2346ef8547b))

- **repo**: Meet ruff config rules
  ([`e18e5bf`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/e18e5bfb10eb4050b1c9b3dfc6a8030a4d7721b2))

- **repo**: Update ruff config
  ([`2905aee`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2905aee66f9e8c2c132594fa29d0a127d02df38c))

### Features

- Improve ruff config
  ([`1380aa8`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/1380aa81c3da3b1941c23a0c759b0af9fbe647ac))


## v0.4.1 (2026-01-27)

### Bug Fixes

- Correct copier min version bumping
  ([`0d53956`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0d539566f7d1a4e1cca496b05e922fca7c775062))

### Chores

- **deps**: Lock file maintenance
  ([`3917a95`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/3917a95775d368b8d5a348fd81a9b4aa6a35b43e))

- **deps**: Lock file maintenance
  ([`4b8f607`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/4b8f6077eab34bdd0c34a1fe28f8fbf4c2e40468))

- **deps**: Pin dependencies
  ([`82168e8`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/82168e87134b534c9fff68af0a775ed428ba3ba2))

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.4.0
  ([`7dc4676`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/7dc46769faaae67169ed28fdeb2273d4bbd44e0f))

- **deps**: Update dependency git@gitlab.com:browniantech/pre-commit-copier-template.git to v0.5.3
  ([`f6f4643`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f6f4643731d61ff5a8aa6da2b267af7300c92f0f))

- **deps**: Update dependency go-task/task to v3.47.0
  ([`fbeb01d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/fbeb01db254e294809052aa9439801602d4d2213))

- **deps**: Update dependency go-task/task to v3.48.0
  ([`2f11400`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/2f11400fc20bfa949b685b0a58afa043112bf0b9))

- **deps**: Update python docker tag to v3.14
  ([`104bbb5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/104bbb5d777bb96a0bf0af772372bb933a0458ac))

- **repo**: Remove duplicate renovate config
  ([`bd221e3`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/bd221e3567acb21ef35d69460edbdf7fe3a4bd7c))


## v0.4.0 (2026-01-25)

### Bug Fixes

- Configure renovate to not pin digests in inner template
  ([`71bc917`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/71bc917dd4eb3588a1877e4e9f16ab25f028356a))

- Correct template name for ci files
  ([`930ff74`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/930ff748ab306cfb95a74ab78a56f72591d93448))

### Chores

- **deps**: Pin dependencies
  ([`a321abb`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/a321abb0e376855de87f4f200025c5d2208a03fc))

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.3.2
  ([`93c3d03`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/93c3d0357de53c926dfcbc06b5894e828ce32026))

### Features

- Deterministic task version updating
  ([`dc1736d`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/dc1736dd02eb611f3c43b28632b2bed78b3da33b))


## v0.3.2 (2026-01-25)

### Features

- Add minimal ruff config to template
  ([`030f6b5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/030f6b5f25d78e83c3a42250916132f5f423aac0))


## v0.3.1 (2026-01-25)

### Bug Fixes

- Correct template name
  ([`dcd34d9`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/dcd34d946023b36b957272c74497c42a5acab0db))


## v0.3.0 (2026-01-25)

### Chores

- **repo**: Update TODO list
  ([`aac13ab`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/aac13ab65b8f899fa9814dee64d219722edae001))

### Features

- Add gitlab ci tests
  ([`ea3647e`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/ea3647e90c5ea5631134edc2cb542f9db1e754a1))

- Enable autoupdate of min copier version
  ([`27b6001`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/27b600157ffa2242f8cc5d3bdd6292b415a25b92))

- Enable choice of template chars
  ([`da32ce5`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/da32ce58e407815305de27b1fc7e13d39944c73a))

- Enable parametrizing test sub_project fixture answers
  ([`0eef2cf`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/0eef2cfa054c88059dcbd0ac7d8bf52ae4eebbac))

- Enable trim_blocks as standard
  ([`22fd850`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/22fd850034a91d712d560b8c462bd9440d76812a))

- Refactor taskfile
  ([`6862f3c`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/6862f3c053c78f56a9d5c832dd1f042397c88e00))


## v0.2.0 (2026-01-25)

### Bug Fixes

- Use frozen lockfile for tests
  ([`6e5492a`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/6e5492adbd3aeee9984fdb5235a519e56e854cd5))

### Chores

- **deps**: Update dependency git@gitlab.com:browniantech/copier-template-copier-template.git to
  v0.1.1
  ([`5280175`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/52801752bb8bb2cfbd71ded8b9d9e2c7cecdfff9))

### Features

- **repo**: Switch template escape characters
  ([`f4362df`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/f4362dffddd6ab5fbdc3d4a6a762f971a7c8d23e))


## v0.1.1 (2026-01-25)

### Bug Fixes

- Update docker example file
  ([`5017f43`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/5017f43cf4ec4ec8bce185a059957b19b9d1861f))

### Chores

- Bump copier template
  ([`40178bf`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/40178bfb568c5593d542d7988008d0b567b87e3c))

- Bump uv lock file
  ([`331d799`](https://gitlab.com/browniantech/copier-template-copier-template/-/commit/331d799a0c01db29f852aa6a8b5c534303047988))


## v0.1.0 (2026-01-25)

- Initial Release
